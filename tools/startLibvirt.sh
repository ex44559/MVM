libvirtd_status=`systemctl is-active libvirtd`
virtlogd_status=`systemctl is-active virtlogd`

if [[ libvirtd_status == "unkown" ]]; then
	/usr/sbin/libvirtd  -d
elif [[ libvirtd_status != "active" ]]; then
	systemctl start libvirtd
else
	echo "libvirtd is running."
fi

if [[ virtlogd_status == "unkown" ]]; then
	/usr/sbin/virtlogd  -d
elif [[ virtlogd_status != "active" ]]; then
	systemctl start virtlogd
else
	echo "libvirtd is running."
fi

