import os
import glob

def combine_txt_files_to_csv(folder_path, output_csv):
    # 폴더 안의 모든 txt 파일 경로 가져오기
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

    # CSV 파일로 데이터 합치기
    with open(output_csv, "w", encoding="utf-8") as csv_file:
        for txt_file in txt_files:
            file_name = os.path.basename(txt_file)
            with open(txt_file, "r", encoding="utf-8") as txt_content:
                lines = txt_content.readlines()
                content = "\n".join(line.strip() for line in lines if line.strip())

                if content:
                    csv_file.write(content + "\n")

    print("모든 txt 파일이 성공적으로 CSV 파일로 합쳐졌습니다.")

# 예시 사용법
folder_path = "./non-translated/EN/"  # 본인이 합치고 싶은 폴더 경로로 변경해야 합니다.
output_csv = "output.csv"    # 합쳐진 데이터를 저장할 CSV 파일 이름

combine_txt_files_to_csv(folder_path, output_csv)
