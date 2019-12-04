#include <iostream>
#include <cmath>
#include <fstream>

const double delta_t= 0.01;
const double delta_x= 0.01;

double init_u(double  x)
{
    return exp(-((x-1)*(x-1))/(2*(0.25*0.25)));
}

double factor(double u,double t,  double x)
{
    return ((1/t)+(1/x))/((1/t)+(u/x));
}

int main(void)
{
    
    std::ofstream file("dif.dat");
    std::ofstream ci("ci.dat");
    int N= 2/delta_x;
    double x= 0.0;
    double uar[N];
    for(double t=0;t<=0.5;t+=delta_t)
    {
        for(int i=0;i<=N;i++)
        {
            if(t==0)
            {
                uar[i]= init_u(x);
                ci<< x << " " <<uar[i]<<std::endl;
            }
            if(t>0)
            {
                uar[i]= uar[i]*factor(uar[i],t,x);
                if(t==0.5)
                {
                    file<< x << " " <<uar[i]<<std::endl;
                }
            }
            x+= delta_x;
        }
    }
    return 0;
}

