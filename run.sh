# Remove old files
#ampy -p /dev/ttyACM0 rmdir Animation/
#ampy -p /dev/ttyACM0 rmdir Led/
#ampy -p /dev/ttyACM0 rmdir Button/
#ampy -p /dev/ttyACM0 rmdir Shared_Informations/
#ampy -p /dev/ttyACM0 rm main.py

# Upload the new files
ampy -p /dev/ttyACM0 put Animation/
ampy -p /dev/ttyACM0 put Led/
ampy -p /dev/ttyACM0 put Button/
ampy -p /dev/ttyACM0 put Shared_Informations/
ampy -p /dev/ttyACM0 put main.py
