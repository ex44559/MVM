#include <stdio.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <linux/kvm.h>

int main(int argc, char const *argv[])
{
        int version;
        int kvm,ret;

        kvm = open( "/dev/kvm", O_RDWR | O_NDELAY );
        version = ioctl( kvm, KVM_GET_API_VERSION, 0 );
        printf("KVM API version is %d\n", version);
        ret = ioctl(kvm,KVM_CHECK_EXTENSION,KVM_CAP_MAX_VCPUS);
        printf("KVM's max vcpu is %d\n", ret);
        return 0;
}
