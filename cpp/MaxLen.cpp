int A=1,B=2,C=9;
vector<pair<int,char>> vec;
vec.push_back(make_pair(A,'A'));
vec.push_back(make_pair(B,'B'));
vec.push_back(make_pair(C,'C'));
sort(vec.begin(),vec.end());
for(int i=0;i<vec.size();i++){
    cout<<"i="<<i<<", first="<<vec[i].first<<", second="<<vec[i].second<<endl;
}
string ans;
//number2 > number1 > number0
if(vec[2].first>=2*(vec[0].first+vec[1].first)){ //number2 > 2*(number0+number1)
    while(vec[2].first>0 && (ans.empty() || ans.back()!=vec[2].second)){
        if(vec[2].first>1){
            ans.push_back(vec[2].second);
            ans.push_back(vec[2].second);
            vec[2].first-=2;
        }else{
            ans.push_back(vec[2].second);
            vec[2].first-=1;
        }
        if(vec[1].first>0){
            ans.push_back(vec[1].second);
            vec[1].first-=1;
        }else if(vec[0].first>0){
            ans.push_back(vec[0].second);
            vec[0].first-=1;
        }
    }
}else if(vec[2].first>=2*vec[1].first){ //number2 > 2*number1
    int extra=vec[2].first-vec[1].first-vec[0].first;
    while(vec[2].first>0 && (ans.empty() || ans.back()!=vec[2].second)){
        if(extra>0){
            ans.push_back(vec[2].second);
            ans.push_back(vec[2].second);
            vec[2].first-=2;
            extra--;
        }else{
            ans.push_back(vec[2].second);
            vec[2].first-=1;
        }
        if(vec[1].first>0){
            ans.push_back(vec[1].second);
            vec[1].first-=1;
        }else if(vec[0].first>0){
            ans.push_back(vec[0].second);
            vec[0].first-=1;
        }
    }
}else{ // number2 < 2*number1
    int extra=vec[2].first-vec[1].first;
    while(vec[2].first>0){
        cout<<"vec[2].first="<<vec[2].first<<", extra="<<extra<<endl;
        if(extra>0){
            ans.push_back(vec[2].second);
            ans.push_back(vec[2].second);
            vec[2].first-=2;
            extra--;
        }else{
            ans.push_back(vec[2].second);
            vec[2].first-=1;
        }
        if(vec[1].first>0){
            ans.push_back(vec[1].second);
            vec[1].first-=1;
        }
        if(vec[0].first>0){
            ans.push_back(vec[0].second);
            vec[0].first-=1;
        }
    }
}
cout<<"ans="<<ans<<endl;
