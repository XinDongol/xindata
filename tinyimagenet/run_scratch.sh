cd /scratch

FILE=/scratch/tiny-imagenet-200/train/n01443537/images/n01443537_164.JPEG
if [ -f "$FILE" ]; then
    echo "tinyimagenet exists in scratch."
else 
    echo "downloading tinyimagenet to scratch"
    rm -rf tiny-imagenet-200
    rm -rf tiny-imagenet-200.zip
    rm -rf tinyimagenet_reformat.py
    
    wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
    unzip tiny-imagenet-200.zip -d ./
    cp /n/holyscratch01/kung_lab/xin/xindata/tinyimagenet/tinyimagenet_reformat.py ./
    python tinyimagenet_reformat.py
fi

