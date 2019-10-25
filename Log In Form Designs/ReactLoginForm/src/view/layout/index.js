import React from 'react'
import '../component/color.css'
import './style.css'

const Layout =(props) => {
	const {children} = props
	return(
		<div className="layout_wrapper">
			{children}
		</div>
		)
}

export default (Layout)