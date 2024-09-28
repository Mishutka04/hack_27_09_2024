// eslint-disable-next-line react/prop-types
export const TextEnter = ({source, onclick}) => {
  return (
    <button className="chat-bot__submit" onClick={onclick}> 
        <img src={source} className='chat-bot__submit__icon' alt="text"/>
    </button>
  )
}
