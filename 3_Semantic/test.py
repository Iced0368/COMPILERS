import os

def compare_files(directory1, directory2):
    # 디렉토리에서 파일 목록 가져오기
    files1 = os.listdir(directory1)
    files2 = os.listdir(directory2)
    cnt = 0

    # 두 디렉토리에서 공통된 파일 이름 찾기
    common_files = sorted(set(files1) & set(files2))

    # 공통된 파일들의 내용 비교
    for file_name in common_files:
        file_path1 = os.path.join(directory1, file_name)
        file_path2 = os.path.join(directory2, file_name)

        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            # 파일 내용이 다를 경우 파일 이름 출력
            if content1 != content2:
                print(file_name)
                cnt += 1
    return cnt

# 비교할 디렉토리 경로 설정
my_result_directory = 'my_result'
test_result_directory = 'testresult'

# 파일 비교 실행
cnt = compare_files(my_result_directory, test_result_directory)
print(cnt)
