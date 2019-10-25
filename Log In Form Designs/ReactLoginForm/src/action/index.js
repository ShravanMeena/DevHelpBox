import {FnsCreator} from '../global/utility'
import {push} from 'react-router-redux'

import login from './login'

const specs = {
    login
}


function ActionCreator(dicts) {
    return FnsCreator(dicts,() => ({ type: "nothing" }))
}

const Modules = Object.keys(specs).reduce((accum, spec) => {
    accum[spec] = ActionCreator(specs[spec])
    return accum
}, {})

export default function Actions(events, ...args) {
    const splitted = events.split('/')
    const module = splitted[0]
    const child = splitted.slice(1).join('/')
    // console.log('actions', events, '-', splitted, '-', module, '-', child, args)

    if (module === "") {
        return (dispatch) => (dispatch({type: child, payload: args[0]}))
    }
    if (module === "push") {
        return (dispatch) => (dispatch(push(args[0])))
    }
    if (module in specs) {
        return Modules[module](child, ...args)
    }
    return () => {}
}


export function RecurringAction(delay, ...args) {
    let intervalID = 0

    function getIntervalID() {
        return intervalID
    }
    return {
        get: getIntervalID,
        fn(dispatch) {
            clearInterval(intervalID)

            function Recurring() {
                dispatch(Actions(...args))
            }
            Recurring()
            intervalID = setInterval(Recurring, delay)
        }
    }
}