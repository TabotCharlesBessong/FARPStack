import { Outlet } from "react-router-dom";
import { Navbar } from "../component";

const MainLayout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export default MainLayout;
