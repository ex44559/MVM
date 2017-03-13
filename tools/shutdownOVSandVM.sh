killVM=$(python /home/sunbo/kvm/MVM/tools/shutdownAllVM.py)

ovsPid=$(cat /usr/local/var/run//openvswitch/ovs-vswitchd.pid 2>/dev/null)
ovsdbPid=$(cat /usr/local/var/run/openvswitch/ovsdb-server.pid 2>/dev/null)
echo $ovsPid

if [ -n "$ovsPid" ]; then 
	kill $ovsPid
	echo "ovs process is killed\n"
else
	echo "ovs isn't running\n"
fi

if [ -n "$ovsdbPid" ]; then
	kill $ovsdbPid
	echo "ovs-db process is killed"
else
	echo "ovsdb isn't running\n"
fi
