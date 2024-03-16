from pydub import AudioSegment

def time_to_ms(time_str):
    parts = time_str.split(":")
    minutes = int(parts[0])
    seconds = float(parts[1])
    milliseconds = int(seconds * 1000)

    total_ms = minutes * 60 * 1000 + milliseconds
    return total_ms

# 오디오 파일 로드
audio = AudioSegment.from_file("../test.mp3")

# 분할할 시간 설정
time_str = "00:21.000"
end_str = "00:27.000"
start_ms = time_to_ms(time_str)
end_ms = time_to_ms(end_str)

# 오디오 분할 및 저장
segment_audio = audio[start_ms:end_ms]
segment_audio.export("test_audio/segment_output.mp3", format="mp3")

print("분할된 오디오가 성공적으로 저장되었습니다.")
