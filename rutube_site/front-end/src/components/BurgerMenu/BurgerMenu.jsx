import './BurgerMenu.style.css';

// eslint-disable-next-line react/prop-types
export const BurgerMenu = ({ toggleMenu }) => {
  return (
    <div className='burger-menu'>
        <button onClick={toggleMenu} type="button" className="burger-menu__btn" aria-label="Открыть меню навигации">
            <svg className="burger-menu__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path fill="white" d="M1.5 3.69c0-.38.268-.69.599-.69H21.9c.331 0 .599.31.599.69 0 .382-.268.691-.599.691H2.1c-.331 0-.599-.309-.599-.69Zm0 8.31c0-.382.268-.69.599-.69H17.4c.33 0 .598.308.598.69s-.268.69-.598.69H2.099c-.331 0-.599-.308-.599-.69m.599 7.619c-.331 0-.599.309-.599.69 0 .382.268.691.599.691H21.9c.331 0 .599-.31.599-.69 0-.382-.268-.691-.599-.691H2.1Z"></path>
            </svg>
        </button>
    </div>
  )
}
