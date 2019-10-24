import React from 'react'
import Layout from '../layout'
import LoginForm from './loginForm'
import './style.css'

const Login = () =>{
	return(
		<Layout>
			<div className='login_wrapper'>
				<LoginForm />
			</div>
		</Layout>
		)
}

export default (Login)