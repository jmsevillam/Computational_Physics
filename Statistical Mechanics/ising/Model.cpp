#include "ising.h"
#include <cstdlib>
#include <cmath>
int main(int argc, char const *argv[]) {
  ising model;
  model.Initial_Conditions(atoi(argv[1]),0.01,0.01);
  int Num=atoi(argv[2]);
  int iter=atoi(argv[3]);

  double dT=(4.0)/((double) Num+1.0);
  double mean_magne;
  double var_magne;
  double counter;
  for (double T=0;T<4;T+=dT){
    model.Temp(T);
    mean_magne=0;
    counter=0;
    for(int i=0;i<iter;i++){
      model.Time_Step();
      if ((float) i/iter>0.9){
        counter+=1.;
        mean_magne+=fabs(model.Magne());
        var_magne+=(model.Magne())*(model.Magne());;
      }
    }
    mean_magne=mean_magne/counter;
    var_magne=var_magne/counter-(mean_magne*mean_magne);
    std::cout<<T<<' '<<mean_magne<<" "<<var_magne<<" "<<var_magne/T<<std::endl;
    }
  return 0;
}
