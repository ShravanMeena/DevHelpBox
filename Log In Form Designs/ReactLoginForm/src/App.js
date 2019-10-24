import React, {Component} from 'react'
import {Provider} from 'react-redux'
import { createBrowserHistory } from 'history'
import StoreCreator from './model'
import AppRoute from './view/route'

class App extends Component {
    render() {
        const history = createBrowserHistory()
        const store = StoreCreator(history)
        return (
            <Provider store={store}>
                <AppRoute history={history} />
            </Provider>
        );
    }
}

export default App;






