import {connect} from 'react-redux'
import {IsArray} from '../global/utility'
import {Map} from 'immutable'

function GetDeep(paths) {
    return (state) => {
        const pathsSplitted = paths.split('/')
        return pathsSplitted.reduce((obj, path) => {
            if (path in obj) return obj[path]
            if (typeof obj.get !== "function") return Map()
            return obj.get(path, Map())
        }, state)
    }
}
function Subs(subscription) {
    const module = subscription.split('/')[0]
    const child = subscription.split('/').slice(1).join('/')
    if (module === "") {
        return GetDeep(child)
    }
    return () => {}
}


function RecursiveDispatcher(dispatch) {
    function Rec(specs) {
        if (typeof specs === "function") {
            return (...args) => (Rec(specs(...args)))
        }
        return dispatch(specs)
    }
    return (initialSpecs) => {
        if(IsArray(initialSpecs)) {
            return () => Rec(initialSpecs)
        }
        return Rec(initialSpecs)
    }
}

export default (selectors = {}, specs = {}) => {
    function StateAccumulator(state, props) {
        const temp = Object.keys(selectors).reduce((accum, name) => {
            accum[name] = Subs(selectors[name])(state, props)
            return accum
        }, {})

        return temp
    }

    function DispatchAccumulator(dispatch) {
        const Dispatcher = RecursiveDispatcher(dispatch)
        return Object.keys(specs).reduce((accum, name) => {
            accum[name] = Dispatcher(specs[name])
            return accum
        }, {})
    }

    return connect(StateAccumulator, DispatchAccumulator)
}
