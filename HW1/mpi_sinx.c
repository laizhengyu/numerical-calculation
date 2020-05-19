#include"mpi.h"
#include<math.h>
#include<stdio.h>

int main(int argc,char *argv[])
{
	int done=0,n,myid,numprocs,i,rc;
	double PI25DT=3.141592653589793238462643;
	double mypi ,pi,h,sum,x,a;
	double res=2.0;
	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD,&myid);
	double local_start,local_finish,total_time;
	while(!done){
		if (myid==0){
			printf("Enter the number of interval:(0 quits)");
			scanf("%d",&n);
			local_start=MPI_Wtime();
		}
		MPI_Bcast(&n,1,MPI_INT,0,MPI_COMM_WORLD);
		if (n==0) break;
		//h=1.0/(double)n;
		h=PI25DT/(double)n;
		sum=0.0;
		for (i=myid+1;i<=n;i+=numprocs)
		{
			x=h*((double)i-0.5);
			sum+=sin(x);
		}
		mypi=h*sum;
		MPI_Reduce(&mypi,&pi,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
		if (myid==0)
		{
			printf("res is %.16f, Error is %.16f\n",pi,fabs(pi-res));
			local_finish=MPI_Wtime();
			total_time=local_finish-local_start;
			printf("Running time is : %.16f \n",total_time);
		}
	}
	MPI_Finalize();
	return 0;
}

