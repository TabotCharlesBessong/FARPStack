import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import MainLayout from "./layout/MainLayout";
import { AddNote, HomePage, NotePage } from "./pages";


const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path="/add-notes" element={<AddNote />} />
        <Route path="/notes-detail" element={<NotePage />} />
      </Route>
    )
  );

  return <RouterProvider router={router} />;
};

export default App;
