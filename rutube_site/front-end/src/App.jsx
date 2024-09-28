import { Header } from '@layout/Header/Header.jsx';
import { Main } from '@layout/Main/Main';

import './App.css'
import { useState } from 'react';

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(true);

  const toggleMenu = () => {
    setIsMenuOpen((prevState) => !prevState);
  }
  
  return (
    <>
      <Header toggleMenu={toggleMenu} />
      <Main isMenuOpen={isMenuOpen} />
    </>
  )
}

export default App
