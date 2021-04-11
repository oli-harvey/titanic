import os
import subprocess
import zipfile

def get_kaggle_data(
        competition: str,
        dir: str = "competition_data"
        ):
    dl_zip = [
        f"mkdir {dir}",
        f"kaggle competitions download -c {competition} -p {dir}",
    ]
    [
       subprocess.Popen(step, shell=True).wait()
       for step in dl_zip
    ]
    zip_path = f"{dir}/{competition}.zip"

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(f"{dir}/")
    
    rm_zip = f"rm {zip_path}"
    subprocess.Popen(rm_zip, shell=True)

    print(f'files downloaded for {competition} competition')
    # print('   ' + os.listdir(dir))
    files = os.listdir(dir)
    [
        print('   ' + file)
        for file in files
    ]
    print(f'located in /{dir}/')