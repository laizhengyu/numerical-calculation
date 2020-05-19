# MPICH
mpich homework1  
编译 mpicc  –g  -Wall –o mpi_hello  mpi_hello.c  
执行 mpiexec  –n <number of processes> ./mpi_hello
-o表示编译成文件输出，执行编译输出的文件即可  
执行sin积分时需要调用Linux的库，因为math.h不在mpi的库里：    
mpicc mpi_sinx.c -lm -o mpi_sinx  
  
  
