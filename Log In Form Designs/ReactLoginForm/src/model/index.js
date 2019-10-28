import {createStore, combineReducers, applyMiddleware} from 'redux'
import {routerReducer, routerMiddleware} from 'react-router-redux'
import thunk from 'redux-thunk'
import Action from '../action'
import {fromJS} from 'immutable'
import {IsArray} from '../global/utility'

import login from './login'
// import {createLogger} from 'redux-logger'
// const logger = createLogger()


function Reducer(moduleName, {initialState, events}) {
    // const {Load, Save} = Storage(name)
    // const loadedState = Load()  

    // let stateUsed = initialState
    // if (specs && loadedState && Validation(specs)(loadedState)) {
    //     stateUsed = loadedState
    // }
    return (state = fromJS(initialState), {type, payload}) => {
        const splittedTypes = type.split('/')
        const actionName = splittedTypes[0]
        const eventName = splittedTypes.slice(1).join('/')
        if (moduleName !== actionName) return state
        if (events &&  eventName in events) return events[eventName](state, payload)
        // if (savedEvent && child in savedEvent) return Save(savedEvent[child](state, payload))
        return state
    }
}

function ReducerCreator(specs) {
    return Object.keys(specs).reduce((accum, name) => {
        accum[name] = Reducer(name, specs[name])
        return accum
    }, {})
}

const ActionMiddleware = Actions => store => next => action => {
    // console.log('act', action)
    if (!IsArray(action)) {
        return next(action)
    }

    if (IsArray(action[0])) {
        return action.forEach((act) => {
            return Actions(...act)(store.dispatch, store.getState)
        })
    }

    return Actions(...action)(store.dispatch, store.getState)
}


const reducerSpecs = {
    login
}

const reducers = ReducerCreator(reducerSpecs)


export default (history) => {
    const routeWithHistory = routerMiddleware(history)

    return createStore(
        combineReducers({
            ...reducers,
            router: routerReducer,
        }),
        applyMiddleware(thunk, ActionMiddleware(Action), routeWithHistory)
        // applyMiddleware(thunk, ActionMiddleware(Action), logger, routeWithHistory)
    )
}
