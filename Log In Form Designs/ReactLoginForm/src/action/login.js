
function ChangeForm(attr, value) {
    return (dispatch) => {
        dispatch(['/login/changeForm', {
        		attr : attr,
        		payload : value
        	}])
    }
}

export default{
	changeForm: ChangeForm,
}