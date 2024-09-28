import './Search.style.css';

export const Search = () => {
  return (
    <div className='search'>
        <svg className="search__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
        <path stroke="white" d="M18 11a6.98 6.98 0 0 1-2.05 4.95A7 7 0 1 1 18 11m2 9-4-4"></path>
        </svg>
        <input className='search__input' type="text" placeholder='Поиск' />
    </div>
  )
}
