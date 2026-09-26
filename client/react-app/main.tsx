import './index.css'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LandingPage from '../react-app/LandingPage'
import App from '../react-app/App'
import { createBrowserRouter, redirect } from "react-router";
import type { LoaderFunction, LoaderFunctionArgs } from "react-router";
import { RouterProvider } from "react-router/dom";

const checkSession: LoaderFunction = async () => {
  
  const rawCookies = document.cookie; 
  
  const match = rawCookies.match(/(?:^|; )Cookie=([^;]*)/);

  if (match == null) {
    return redirect("/")
  }

  return true;
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage/>,
  }, 
  {
    path: "/home",
    element: <App/>,
    loader: checkSession
  }
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router}/>
  </StrictMode>,
)
