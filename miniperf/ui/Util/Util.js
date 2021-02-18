import React, {useEffect, useRef} from "react";

export function useInterval(callback, delay) {
    const savedCallback = useRef();

    // Remember the latest callback.
    useEffect(() => {
        savedCallback.current = callback;
    });

    // Set up the interval.
    useEffect(() => {
        function tick() {
            savedCallback.current();
        }
        if (delay !== null) {
            let id = setInterval(tick, delay);
            return () => clearInterval(id);
        }
    }, [delay]);
}

export const useUpdate = (fn, dep)=>{
    const [count,setCount] = React.useState(0)
    useEffect(()=>{
        setCount(x => x + 1);
    },[dep])
    useEffect(()=>{
        if(count > 1){
            fn()
        }
    },[count,fn])
}