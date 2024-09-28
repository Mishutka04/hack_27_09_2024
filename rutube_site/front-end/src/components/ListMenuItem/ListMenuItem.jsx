import './ListMenuItem.style.css';

// eslint-disable-next-line react/prop-types
export const ListMenuItem = ({svg, text, isOpened=true}) => {
  return (
    <li className={`list-menu-item ${isOpened ? 'opened' : 'closed'}`}>
        <div className="list-menu-item__icon">
            <img className='list-menu-item__icon__img' src={svg} />
        </div>
        <div className="list-menu-item__text">
            <span>{text}</span>
        </div>
    </li>
  )
}