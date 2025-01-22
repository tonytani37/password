import os

def delete_json_files(directory):
  """
  指定されたフォルダ内の全てのJSONファイルを削除します。

  Args:
    directory: 削除対象のフォルダパス

  Returns:
    None
  """
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith(".json"):
        file_path = os.path.join(root, file)
        os.remove(file_path)
        # print(f"削除しました: {file_path}")

# 削除したいフォルダのパスを指定

target_directory = "/Volumes/WD02/写真移行/Takeout 8/Google フォト"

# 関数を実行
print('はじめ')
delete_json_files(target_directory)
print('おわり')