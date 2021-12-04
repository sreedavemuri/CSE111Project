import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Valorant</h1>
      <div className="Tables">
        <button class="button">Agents</button>
        <button class="button">Weapons</button>
        <button class="button">Roles</button>
        <button class="button">KDA</button>
        <button class="button">Map</button>
        <button class="button">Origin</button>
        <button class="button">MapRank</button>
      </div>

      <br></br>

      <div className="Dropdown">
        <label>Role: </label>
        <select name="Roles" id="Roles">
          <option value="0">--Select--</option>
          <option value="1">Controller</option>
          <option value="2">Duelist</option>
          <option value="3">Initiator</option>
          <option value="4">Sentinel</option>
        </select>

        <label>Map: </label>
        <select name="Maps" id="Maps">
          <option value="0">--Select--</option>
          <option value="1">Split</option>
          <option value="2">Bind</option>
          <option value="3">Ascent</option>
          <option value="4">Icebox</option>
          <option value="4">Breeze</option>
          <option value="4">Haven</option>
        </select>
      </div>
    </div>
  );
}

export default App;
