import os
import argparse
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment, silence

def detect_silence(audio_segment, min_silence_len=1000, silence_thresh=-30):
    return silence.detect_silence(audio_segment, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

def merge_close_segments(segments, max_gap=1000):
    merged = []
    for segment in segments:
        if not merged or segment[0] - merged[-1][1] > max_gap:
            merged.append(segment)
        else:
            merged[-1] = (merged[-1][0], segment[1])
    return merged

def remove_silence(input_path, output_path, temp_dir, min_silence_len=350, silence_thresh=-30, padding_duration=100, max_gap=100):
    temp_audio_path = os.path.join(temp_dir, "temp_audio.wav")

    try:
        os.makedirs(temp_dir, exist_ok=True)

        video = VideoFileClip(input_path)
        audio = video.audio
        audio.write_audiofile(temp_audio_path)

        audio_segment = AudioSegment.from_wav(temp_audio_path)
        silence_ranges = detect_silence(audio_segment, min_silence_len, silence_thresh)

        non_silent_segments = []
        prev_end = 0
        for start, end in silence_ranges:
            if prev_end < start:
                non_silent_segments.append((prev_end, start))
            prev_end = end

        if prev_end < len(audio_segment):
            non_silent_segments.append((prev_end, len(audio_segment)))

        merged_segments = merge_close_segments(non_silent_segments, max_gap)

        final_segments = [(max(0, start - padding_duration), min(len(audio_segment), end + padding_duration)) for start, end in merged_segments]

        non_silent_clips = [video.subclip(start / 1000.0, end / 1000.0) for start, end in final_segments]
        final_video = concatenate_videoclips(non_silent_clips)
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        video.close()

def main():
    parser = argparse.ArgumentParser(description="SilenceCutter - A tool to remove silent parts from video files.")
    parser.add_argument("--input", required=True, help="Path to the input video file")
    parser.add_argument("--output", required=True, help="Path to the output video file")
    parser.add_argument("--temp_dir", default="./temp", help="Path to the temporary directory")
    parser.add_argument("--min_silence_len", type=int, default=350, help="Minimum silence length in milliseconds")
    parser.add_argument("--silence_thresh", type=int, default=-30, help="Silence threshold in dB")
    parser.add_argument("--padding_duration", type=int, default=100, help="Padding duration in milliseconds for smooth transitions")
    parser.add_argument("--max_gap", type=int, default=100, help="Maximum gap in milliseconds to merge segments")
    parser.add_argument("--version", action="version", version="SilenceCutter 1.0")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}")
        return

    temp_dir = "./temp"
    if os.path.exists(args.temp_dir):
        temp_dir = args.temp_dir

    os.makedirs(temp_dir, exist_ok=True)

    if args.verbose:
        print(f"Input file: {args.input}")
        print(f"Output file: {args.output}")
        print(f"Temporary directory: {args.temp_dir}")
        print(f"Minimum silence length: {args.min_silence_len} ms")
        print(f"Silence threshold: {args.silence_thresh} dB")
        print(f"Padding duration: {args.padding_duration} ms")
        print(f"Maximum gap: {args.max_gap} ms")

    remove_silence(args.input, args.output, args.temp_dir, args.min_silence_len, args.silence_thresh, args.padding_duration, args.max_gap)

    os.rmdir(temp_dir)

if __name__ == "__main__":
    main()
