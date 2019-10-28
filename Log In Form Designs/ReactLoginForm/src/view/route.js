import React from 'react'
import {Router, Switch, Route} from 'react-router'
import Login from './login'

function Root({history}) {
	return(
		<Router history={history}>
		 	<Switch>
            	<Route path="*" component={Login} />    
   			</Switch>
       	</Router>
		)
}


export default Root