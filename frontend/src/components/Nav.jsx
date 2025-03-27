import { FaInstagram } from 'react-icons/fa';
import { useState } from 'react';

const Navbar = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="bg-gradient-to-r from-purple-600 to-pink-600 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo/Brand */}
          <div className="flex-shrink-0 flex items-center">
            <FaInstagram className="h-8 w-8 text-white" />
            <span className="ml-2 text-white text-xl font-bold">
              Reel<span className="text-yellow-300">Downloader</span>
            </span>
          </div>

          {/* Navigation Links - Hidden on mobile, shown on md+ */}
          <div className="hidden md:block">
            <div className="ml-10 flex items-center space-x-4">
              <a
                href="https://www.loom.com/share/601a799697b047fdb1a146638e8b97a9" target='_blank'
                className="text-white hover:bg-purple-700 hover:bg-opacity-50 px-3 py-2 rounded-md text-sm font-medium"
              >
                How to Use
              </a>
              <a
                href="#"
                className="text-white hover:bg-purple-700 hover:bg-opacity-50 px-3 py-2 rounded-md text-sm font-medium"
              >
                FAQ
              </a>
              <a
                href="#"
                className="text-white hover:bg-purple-700 hover:bg-opacity-50 px-3 py-2 rounded-md text-sm font-medium"
              >
                Contact
              </a>
            </div>
          </div>

          {/* Mobile menu button */}
          <div className="-mr-2 flex md:hidden">
            <button
              type="button"
              onClick={toggleMobileMenu}
              className="bg-purple-700 inline-flex items-center justify-center p-2 rounded-md text-white hover:text-white hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-purple-800 focus:ring-white"
              aria-controls="mobile-menu"
              aria-expanded={isMobileMenuOpen}
            >
              <span className="sr-only">Open main menu</span>
              {/* Hamburger icon */}
              <svg
                className={`h-6 w-6 ${isMobileMenuOpen ? 'hidden' : 'block'}`}
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
              {/* Close icon */}
              <svg
                className={`h-6 w-6 ${isMobileMenuOpen ? 'block' : 'hidden'}`}
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu, show/hide based on menu state */}
      <div className={`md:hidden ${isMobileMenuOpen ? 'block' : 'hidden'}`} id="mobile-menu">
        <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <a
            href="https://www.loom.com/share/601a799697b047fdb1a146638e8b97a9" target='_blank'
            className="text-white hover:bg-purple-700 hover:bg-opacity-50 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            How to Use
          </a>
          <a
            href="#"
            className="text-white hover:bg-purple-700 hover:bg-opacity-50 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            FAQ
          </a>
          <a
            href="#"
            className="text-white hover:bg-purple-700 hover:bg-opacity-50 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            Contact
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;