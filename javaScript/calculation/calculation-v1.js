function calculation(){//定义计算函数
    var x=document.getElementById("x-value").value;//定义x并将用户输入的x赋值给它
    var y=document.getElementById("y-value").value;//定义y并将用户输入的y赋值给它
    var index=document.getElementById("yunsuanfu").selectedIndex;//获取操作符的索引
    var my_select=document.getElementById("yunsuanfu").options;//获取下拉框这个对象
    switch(index)
        {
            case 0:
                result=parseInt(x)+parseInt(y)
                document.getElementById("jieguo").value=result;//将结果输出到文本框
                break;
            case 1:
                result=parseInt(x)-parseInt(y);
                document.getElementById("jieguo").value=result;
                break;
            case 2:
                result=parseInt(x)*parseInt(y);
                document.getElementById("jieguo").value=result;
                break;
            case 3:
                result=parseInt(x)/parseInt(y);
                document.getElementById("jieguo").value=result;
                break;
        }
    }  