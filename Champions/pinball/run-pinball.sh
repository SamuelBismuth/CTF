KEY_PY=$1
KEY_PX=$2
KEY_VY=$3
KEY_VX=$4

echo $KEY_PY
echo $KEY_PX
echo $KEY_VY
echo $KEY_VX

./pinball.elf transform "msg.enc" "out.txt" $KEY_PY $KEY_PX $KEY_VY $KEY_VX
 
