/**
 * Created by interpolar on 9/24/15.
 */
function numChk()
    {
        var count = document.getElementById('emp_count').value
        var num_check=/^[0-9]*$/
        var frm = document.frm
        alert(count.value)
        if(count = ""){
            alert('인원을 입력하여 주세요.')
            return false
        }
        if(num_check.test(count)){
            alert('숫자만 입렵해 주세요')
            return false
        }
        else if(parseInt(count) == true){
            alert(count)
            frm.action = "input/pinfo"
            return true
        }
    }
