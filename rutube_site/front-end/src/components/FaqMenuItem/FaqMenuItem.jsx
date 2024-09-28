import './FaqMenuItem.style.css';

// eslint-disable-next-line react/prop-types
export const FaqMenuItem = ({text, isActive=false}) => {
  return (
    <li className={`${isActive ? 'blue-btn-active' : 'blue-btn-inactive'} faq-menu__item`}>
        <span>{text}</span>
    </li>
  )
}
