for i in {1..100}; do
dd if=/dev/urandom of=/home/sainikhil/mnt/2GB_volume.img/file_$i bs=1M count=10
done
