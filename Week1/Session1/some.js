function ascendingLikeValues(arr){
    var strOne=arr[0].split(',');
    var strTwo=arr[1].split(',');
    var retStr="";
    if(strOne.length>strTwo.length){
        var large=strOne;
        var small=strTwo;
    } else {
        var large=strTwo;
        var small=strOne;
    }
    for(let i=0; i<small.length; i++){
        for(let j=0; j<large.length; j++){
            if(small[i]==large[j]){
                retStr+=small[i];
            }
        }
    }
    if(retStr.length==0){
        return false
    }
    return retStr
}

console.log(ascendingLikeValues(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))