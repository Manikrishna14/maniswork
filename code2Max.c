#include<stdio.h>
int main()
{
	int i,j,r,c,a[10][10],s;
	printf("Enter no. of rows and columns : ");
	scanf("%d%d",&r,&c);
	printf("Enter the matrix\n");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		scanf("%d",&a[i][j]);
	}
	int m=a[0][0],row;
	for(i=0;i<r;i++)
	{
		s=0;
		for(j=0;j<c;j++)		
		{
			s+=a[i][j];
		}
		if(m<s)
		{
			m=s;
			row=i;
		}
	}
	printf("Row with maximum sum is %d with sum=%d",row+1,m);
}