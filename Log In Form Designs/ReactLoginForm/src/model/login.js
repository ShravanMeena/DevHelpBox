

const initialState = {
	login: {
		username: '',
		password: ''
	}
}

const events = {
	changeForm :(state, action) => (state.updateIn(['login', action.attr], val => action.payload)),
}

export default {
	initialState, events
}