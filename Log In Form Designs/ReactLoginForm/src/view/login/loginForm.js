import React from 'react'
import Button from '../component/button'
import Connect from '../connect'
import {GetAttrs} from '../../global/utility'
import './style.css'

const LoginForm = (props) =>{
	const [username, pass] = GetAttrs(props.login,['username', 'password'])
	return(
		<div className='login_form'>
			<div className='login_title'>
				Login
			</div>
			<div className='login_inputForm'>
				<div className='login_inputTitle'>Username </div>
				<input type='text' className='login_inputBox' placeholder="username" value={username} onChange={props.ChangeForm('username')}/>
			</div>
			<div className='login_inputForm'>
				<div className='login_inputTitle'>Password </div>
				<input type='password' className='login_inputBox' placeholder="password" value={pass} onChange={props.ChangeForm('password')}/>
			</div>
			<div className='login_buttonWrapper'>
				<Button custom={'login_okButton'} content={'Login'} Action={props.ToDashboard}/>
			</div>
		</div>
		)
}
const states={
	login : '/login/login',
}
const actions={
	ChangeForm :(attr) => (e)=> (['login/changeForm', attr, e.target.value]),
	ToDashboard : () => (['push', `/dashboard`])
}

export default Connect(states, actions)(LoginForm)