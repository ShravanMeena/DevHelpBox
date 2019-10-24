export function FnsCreator(dicts, defaultReturn) {
    return (events, ...args) => {
        if (events in dicts) {
            return dicts[events](...args)
        }
        return defaultReturn;
    }
}

export function GetAttrs(immutableObj, attrs) {
    if (!immutableObj) {
        return []
    }
    return attrs.map((s) => ((typeof immutableObj.get) && immutableObj.get(s)))
}


export function ToSimpleTime(date) {
    const d = new Date(date)
    return `${d.getDate()}/${d.getMonth() + 1}/${d.getFullYear()} ${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}`
}

export function GetElapsedTime(prevDate) {
    const prev = new Date(prevDate)
    const now = new Date()
    let diff = Math.round((now - prev) / 1000)

    if (diff < 60) return `${diff} detik yang lalu`

    diff = Math.round(diff/60)
    if (diff < 60) return `${diff} menit yang lalu`

    diff = Math.round(diff/60)
    if (diff < 24) return `${diff} jam yang lalu`

    diff = Math.round(diff/24)
    if (diff < 30) return `${diff} hari yang lalu`

    return ToSimpleTime(prevDate)
}

export function ToPrice(x) {
    if (!x) {
        return '0';
    }
    return x.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");
}

export function ToTitleCase(s) {
    return s.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

export function ToStartOfDay(date) {
    let d = new Date(date)
    d.setHours(0)
    d.setMinutes(0)
    d.setSeconds(0)

    return d
}

export function ToEndOfDay(date) {
    let d = new Date(date)
    d.setDate(d.getDate() + 1)
    return ToStartOfDay(d)
}

export function TimeFormatter(time){
    const monthList = ['Januari', 'Febuari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    const dayList = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    const timesplitted = time.split('T')
    const currentTime = new Date()

    const year = parseInt(timesplitted[0].split('-')[0], 10)
    const month = parseInt(timesplitted[0].split('-')[1], 10)
    const date = parseInt(timesplitted[0].split('-')[2], 10)

    const hourscnd = timesplitted[1].split('+')
    const hour = parseInt(hourscnd[0].split(':')[0], 10)
    const hourString = hourscnd[0].split(':')[0]
    const min = parseInt(hourscnd[0].split(':')[1], 10)
    const minString = hourscnd[0].split(':')[1]

    const monthString = monthList[month - 1]
    const yeardate = new Date(year, month-1, date, hour, min)
    const dayString = dayList[yeardate.getDay()]

    function a () {
        const diff = currentTime - yeardate
        if (diff / 31556952000 >= 1)
            return Math.floor(diff / 31556952000) + " tahun yang lalu"
        if (diff / 2629746000 >= 1)
            return Math.floor(diff / 2629746000) + " bulan yang lalu"
        if (diff / 604800000 >= 1)
            return Math.floor(diff / 604800000) + " minggu yang lalu"
        if (diff / 86400000 >= 1)
            return Math.floor(diff / 86400000) + " hari yang lalu"
        if (diff / 3600000 >= 1)
            return Math.floor(diff / 3600000) + " jam yang lalu"
        if (diff / 60000 >= 1)
            return Math.floor(diff / 60000) + " menit yang lalu"
        return 0
    }

    const additional = a()
    const completeTime = {
        time : yeardate,
        min : minString,
        hour : hourString,
        date : date,
        month : month,
        year : year,
        dayName : dayString,
        monthName :monthString,
        additional : additional
    }

    return completeTime;
}

export function IsArray(arr) {
    return (Object.prototype.toString.call(arr) === '[object Array]')
}

export function ProjectObj(attrs) {
    return (obj) => {
        return attrs.reduce((accum, attr) => {
            accum[attr] = obj[attr]
            return accum
        }, {})
    }
}

export function ExpandObjs(_objs, expansion) {
    const objs = IsArray(_objs) ? _objs : [_objs]
    return objs.map((obj) => (Object.assign({}, obj, expansion)))
}

export function ArrToObj(arr, identityFn) {
    return arr.reduce((accum, obj) => {
        accum[identityFn(obj)] = obj
        return accum
    }, {})
}

export function ProjectArr(arr, ids, identityFn = (x) => (x)) {
    const filteredArr = arr.filter((obj) => (ids.indexOf(identityFn(obj)) > -1))
    const obj = ArrToObj(filteredArr, identityFn)
    return ids.map((id) => (obj[id]))
}

export function Compose(fn, ...fns) {
    return (...args) => {
        return fns.reduce((accum, nextFn) => (nextFn(accum)), fn(...args))
    }
}