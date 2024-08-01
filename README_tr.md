# SilenceCutter

SilenceCutter, video dosyalarındaki sessiz kısımları otomatik olarak tespit edip kaldırarak daha akıcı ve kesintisiz videolar oluşturmanıza olanak tanıyan bir Python uygulamasıdır. 

## Özellikler

- **Sessizlik Tespiti:** Videodaki sessiz bölümleri tespit eder.
- **Sessiz Kısımları Kaldırma:** Sessiz kısımları kaldırarak videoyu daha akıcı hale getirir.
- **Yakın Segmentleri Birleştirme:** Birbirine yakın sessiz olmayan segmentleri birleştirir.
- **Yumuşak Geçişler:** Segmentlerin başına ve sonuna eklenen padding süreleri ile kesme işlemini yumuşatır.
- **Kullanıcı Dostu:** Basit ve anlaşılır bir kullanım sunar.

## Gereksinimler

- Python 3.x
- moviepy
- pydub

## Kurulum

```bash
pip install silencecutpy
```

## Kullanım

```bash
silencecutpy --input project/silencecut-py/example_input.mp4 --output output.mp4
```

## Parametreler
- `--input`: Giriş video dosyası
- `--output`: Çıkış video dosyası
- `--silence_threshold`: Sessizlik eşik değeri (varsayılan: -30)
- `--min_silence_length`: Minimum sessizlik süresi (varsayılan: 350)
- `--padding_duration`: Yumuşak geçiş süresi (varsayılan: 100)
- `--max_gap`: Birleştirilecek maksimum segment aralığı (varsayılan: 100)
- `--temp_dir`: Geçici dosyaların kaydedileceği dizin
- `--verbose`: Ayrıntılı çıktıları gösterir

## Örnek

```bash
python silence_cutter.py --input video.mp4 --output video_silence_removed.mp4 --silence_threshold -30 --min_silence_length 350 --padding_duration 100 --max_gap 100 --temp_dir temp
```