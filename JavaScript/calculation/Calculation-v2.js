function calculation(){//定义计算函数
    var x=document.getElementById("x-value").value;//定义x并将用户输入的x赋值给它
    
    var y=document.getElementById("y-value").value;//定义y并将用户输入的y赋值给它
    if(!x||!y){
        alert("输入不合法");//x或y为空时提示输入不合法
        return ;
    }
    var index=document.getElementById("yunsuanfu").selectedIndex;//获取操作符的索引
    var my_select=document.getElementById("yunsuanfu").options;//获取下拉框这个对象
    switch(index)
        {
            case 0:
                result=parseFloat(parseFloat(x)+parseFloat(y)).toFixed(2);
                //先将x和y分别转为浮点数 再将运算结果转化为浮点数 用toFixed方法保证结果保留两位小数
                document.getElementById("jieguo").value=result;//将结果输出到文本框
                break;
            case 1:
                result=parseFloat(parseFloat(x)-parseFloat(y)).toFixed(2);
                document.getElementById("jieguo").value=result;
                break;
            case 2:
                result=parseFloat(parseFloat(x)*parseFloat(y)).toFixed(2);
                document.getElementById("jieguo").value=result;
                break;
            case 3:
                result=parseFloat(parseFloat(x)/parseFloat(y)).toFixed(2);
                document.getElementById("jieguo").value=result;
                break;
        }
    }  
