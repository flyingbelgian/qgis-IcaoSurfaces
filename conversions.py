def ft2m(x):
    return x * 0.3048

def m2ft(x):
    return x / 0.3048

def NM2m(x):
    return x * 1852

def m2NM(x):
    return x / 1852

def define_reference_system(runway_start, runway_end):
    """
    Define the reference system based on the runway.
    Args:
        runway_start (tuple): (easting, northing) coordinates of the runway start (threshold).
        runway_end (tuple): (easting, northing) coordinates of the runway end.
    
    Returns:
        dict: A dictionary containing the origin, unit vectors for x and y axes.
    """
    # Extract coordinates
    x1, y1 = runway_start
    x2, y2 = runway_end
    # Calculate the direction vector of the runway centerline
    dx = x2 - x1
    dy = y2 - y1
    runway_length = (dx**2 + dy**2)**0.5
    # Unit vector along the runway (x-axis)
    ux = dx / runway_length
    uy = dy / runway_length
    # Unit vector perpendicular to the runway (y-axis)
    vx = -uy  # Rotate 90 degrees clockwise
    vy = ux
    # Return the reference system components
    return {
        "origin": (x1, y1),   # Runway start is the origin
        "x_unit": (ux, uy),   # Unit vector for x-axis
        "y_unit": (vx, vy)    # Unit vector for y-axis
    }

def convert_to_xy(object_coords, reference_system):
    """
    Convert object coordinates (easting, northing) to the x, y reference system.
    Args:
        object_coords (tuple): (easting, northing) coordinates of the object.
        reference_system (dict): Reference system defined by `define_reference_system`.
    Returns:
        tuple: (x, y) coordinates in the reference system.
    """
    # Extract reference system components
    origin = reference_system["origin"]
    x_unit = reference_system["x_unit"]
    y_unit = reference_system["y_unit"]
    # Calculate the vector from the origin to the object
    dx = object_coords[0] - origin[0]
    dy = object_coords[1] - origin[1]
    # Project onto the x and y unit vectors
    x = dx * x_unit[0] + dy * x_unit[1]  # Dot product with x-axis unit vector
    y = dx * y_unit[0] + dy * y_unit[1]  # Dot product with y-axis unit vector
    return (x, y)

def convert_to_easting_northing(object_xy, reference_system):
    """
    Convert (x, y) coordinates in the runway reference system back to easting and northing.
    Args:
        object_xy (tuple): (x, y) coordinates in the runway reference system.
        reference_system (dict): Reference system defined by `define_reference_system`.
    Returns:
        tuple: (easting, northing) coordinates in the original system.
    """
    # Extract reference system components
    origin = reference_system["origin"]
    x_unit = reference_system["x_unit"]
    y_unit = reference_system["y_unit"]
    # Extract the x and y coordinates in the reference system
    x, y = object_xy
    # Compute the easting and northing using the reference system
    easting = origin[0] + x * x_unit[0] + y * y_unit[0]
    northing = origin[1] + x * x_unit[1] + y * y_unit[1]
    return (easting, northing)

def distance_2pts(pta, ptb):
    pta_x, pta_y = pta
    ptb_x, ptb_y = ptb
    dist = ( (ptb_x-pta_x)**2 + (ptb_y-pta_y)**2 ) ** 0.5
    return dist