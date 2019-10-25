import React from 'react'
import './style.css'

function Button({custom, content, isLoading=false, Action}){
	const loading = "/img/spinner.gif"
	return(
		<div className={'button_wrapper '+ custom}>
		{ 
			isLoading ?
			<div> Loading <img alt="null" src={loading} className='button_loading'/></div>
			:
			<div onClick={Action}> {content}</div>
		}
		</div>
	)
}
export default Button