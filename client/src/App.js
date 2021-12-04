import './App.css';

function App() {
  return (
    <div className="App">
      <div className="Information">
        <button class="button">Agents</button>
        <button class="button">Weapons</button>
        <button class="button">Roles</button>
        <button class="button">KDA</button>
        <button class="button">Map</button>
        <button class="button">Origin</button>
        <button class="button">MapRank</button>
      </div>

      <div className="Dropdown">
        <label>Roles:</label>
        <select name="Roles" id="Roles">
          <option value="0">--Select--</option>
          <option value="1">Controller</option>
          <option value="2">Duelist</option>
          <option value="3">Initiator</option>
          <option value="4">Sentinel</option>
        </select>
      </div>
    </div>
  );
}

export default App;
