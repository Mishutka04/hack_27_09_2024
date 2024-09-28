import './Header.style.css';
import { LeftMenu } from './LeftMenu/LeftMenu.jsx';
import { Search } from '@components/Search/Search.jsx';
import { RightMenu } from './RightMenu/RightMenu.jsx';
import { useMediaQuery } from 'react-responsive';

// eslint-disable-next-line react/prop-types
export const Header = ({ toggleMenu }) => {
  const isTablet = useMediaQuery({query: '(max-width: 1024px)'});

  return (
    <header className='header'>
        <LeftMenu toggleMenu={toggleMenu}/>
        {isTablet ? null : <Search />}
        <RightMenu />
    </header>
  )
}
