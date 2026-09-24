int fun(int arr){
        max = arr[0];
        for(int i=1; i<7; i++ ){
            if(arr[i]>max){
                max = arr[i];
            };
        };
        return max;
    };